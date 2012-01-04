%global packname  IdMappingRetrieval
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          ID Mapping Data Retrieval

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.oo R-XML R-RCurl R-rChoiceDialogs R-ENVISIONQuery 
Requires:         R-biomaRt R-ENVISIONQuery R-DAVIDQuery R-AffyCompatible R-R.methodsS3 R-R.oo R-utils 

BuildRequires:    R-devel tex(latex) R-R.oo R-XML R-RCurl R-rChoiceDialogs R-ENVISIONQuery
BuildRequires:    R-biomaRt R-ENVISIONQuery R-DAVIDQuery R-AffyCompatible R-R.methodsS3 R-R.oo R-utils 


%description
Data retrieval for identifier mapping performance analysis

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora