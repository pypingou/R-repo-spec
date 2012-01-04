%global packname  AffyCompatible
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          Affymetrix GeneChip software compatibility

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-XML R-RCurl R-methods 
Requires:         R-Biostrings 

BuildRequires:    R-devel tex(latex) R-XML R-RCurl R-methods
BuildRequires:    R-Biostrings 


%description
This package provides an interface to Affymetrix chip annotation and
sample attribute files. The package allows an easy way for users to
download and manage local data bases of Affynmetrix NetAffx annotation
files. The package also provides access to GeneChip Operating System
(GCOS) and GeneChip Command Console (AGCC)-compatible sample annotation

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora