%global packname  speff2trial
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Semiparametric efficient estimation for a two-sample treatment effect

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-leaps R-survival 

BuildRequires:    R-devel tex(latex) R-leaps R-survival 

%description
The package performs estimation and testing of the treatment effect in a
2-group randomized clinical trial with a quantitative, dichotomous, or
right-censored time-to-event endpoint. The method improves efficiency by
leveraging baseline predictors of the endpoint. The inverse probability
weighting technique of Robins, Rotnitzky, and Zhao (JASA, 1994) is used to
provide unbiased estimation when the endpoint is missing at random.

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
%doc %{rlibdir}/speff2trial/DESCRIPTION
%doc %{rlibdir}/speff2trial/html
%{rlibdir}/speff2trial/data
%{rlibdir}/speff2trial/NAMESPACE
%{rlibdir}/speff2trial/help
%{rlibdir}/speff2trial/R
%{rlibdir}/speff2trial/Meta
%{rlibdir}/speff2trial/INDEX

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora