%global packname  panp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Presence-Absence Calls from Negative Strand Matching Probesets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-Biobase 
Requires:         R-Biobase R-methods R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-affy R-Biobase
BuildRequires:    R-Biobase R-methods R-stats R-utils 


%description
A function to make gene presence/absence calls based on distance from
negative strand matching probesets (NSMP) which are derived from
Affymetrix annotation. PANP is applied after gene expression values are
created, and therefore can be used after any preprocessing method such as
MAS5 or GCRMA, or PM-only methods like RMA. NSMP sets have been
established for the HGU133A and HGU133-Plus-2.0 chipsets to date.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora