%global packname  frailtyHL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Frailty Models via H-likelihood

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-numDeriv 

BuildRequires:    R-devel tex(latex) R-Matrix R-numDeriv 

%description
The frailtyHL package implements the h-likelihood estimation procedures
for frailty models. The package fits Cox's proportional hazards models
with random effects (or frailties). For the frailty distribution lognormal
and gamma are allowed. The h-likelihood uses the Laplace approximation
when the numerical integration is intractable, giving a statistically
efficient estimation in frailty models.

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
%doc %{rlibdir}/frailtyHL/DESCRIPTION
%doc %{rlibdir}/frailtyHL/html
%{rlibdir}/frailtyHL/R
%{rlibdir}/frailtyHL/NAMESPACE
%{rlibdir}/frailtyHL/INDEX
%{rlibdir}/frailtyHL/Meta
%{rlibdir}/frailtyHL/help
%{rlibdir}/frailtyHL/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora