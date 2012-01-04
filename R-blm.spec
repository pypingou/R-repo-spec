%global packname  blm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.2.0
Release:          1%{?dist}
Summary:          Binomial linear and linear-expit regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-methods R-BB R-MASS R-numDeriv R-alabama 

BuildRequires:    R-devel tex(latex) R-stats R-methods R-BB R-MASS R-numDeriv R-alabama 

%description
General additive regression models for binary cohort data which use
constrained maximum likelihood for estimation.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.2.0-1
- initial package for Fedora