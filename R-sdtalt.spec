%global packname  sdtalt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Signal detection theory and alternatives

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lme4 R-boot 


BuildRequires:    R-devel tex(latex) R-lme4 R-boot



%description
Signal detection theory and alternatives

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
%doc %{rlibdir}/sdtalt/DESCRIPTION
%doc %{rlibdir}/sdtalt/html
%{rlibdir}/sdtalt/data
%{rlibdir}/sdtalt/R
%{rlibdir}/sdtalt/NAMESPACE
%{rlibdir}/sdtalt/INDEX
%{rlibdir}/sdtalt/help
%{rlibdir}/sdtalt/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora