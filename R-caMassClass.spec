%global packname  caMassClass
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9
Release:          1%{?dist}
Summary:          Processing & Classification of Protein Mass Spectra (SELDI) Data

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-PROcess R-e1071 R-nnet R-rpart R-caTools R-XML R-digest R-MASS 


BuildRequires:    R-devel tex(latex) R-PROcess R-e1071 R-nnet R-rpart R-caTools R-XML R-digest R-MASS



%description
Functions for processing and classification of protein mass spectra
(SELDI) data. Also includes support for mzXML Files.

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
%doc %{rlibdir}/caMassClass/html
%doc %{rlibdir}/caMassClass/DESCRIPTION
%doc %{rlibdir}/caMassClass/doc
%{rlibdir}/caMassClass/Test
%{rlibdir}/caMassClass/R
%{rlibdir}/caMassClass/Meta
%{rlibdir}/caMassClass/INDEX
%{rlibdir}/caMassClass/NAMESPACE
%{rlibdir}/caMassClass/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9-1
- initial package for Fedora