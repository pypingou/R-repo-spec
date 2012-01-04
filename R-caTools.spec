%global packname  caTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12
Release:          1%{?dist}
Summary:          Tools: moving window statistics, GIF, Base64, ROC AUC, etc.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-bitops 


BuildRequires:    R-devel tex(latex) R-bitops



%description
Contains several basic utility functions including: moving (rolling,
running) window statistic functions, read/write for GIF and ENVI binary
files, fast calculation of AUC, LogitBoost classifier, base64
encoder/decoder, round-off error free sum and cumsum, etc.

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
%doc %{rlibdir}/caTools/DESCRIPTION
%doc %{rlibdir}/caTools/html
%{rlibdir}/caTools/R
%{rlibdir}/caTools/NAMESPACE
%{rlibdir}/caTools/INDEX
%{rlibdir}/caTools/help
%{rlibdir}/caTools/libs
%{rlibdir}/caTools/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12-1
- initial package for Fedora