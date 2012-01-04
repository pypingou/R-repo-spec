%global packname  timereg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.6
Release:          1%{?dist}
Summary:          timereg package for Flexible regression models for survival data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Programs for Martinussen and Scheike (2006), `Dynamic Regression Models
for Survival Data', Springer Verlag.  Plus more recent developments.
Additive survival model, semiparametric proportional odds model,
cumulative residuals, excess risk models and more. Flexible competing
risks regression including GOF-tests. Two-stage frailty modelling. PLS and
Lasso for the additive risk model.

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
%doc %{rlibdir}/timereg/html
%doc %{rlibdir}/timereg/CITATION
%doc %{rlibdir}/timereg/DESCRIPTION
%{rlibdir}/timereg/INDEX
%{rlibdir}/timereg/NAMESPACE
%{rlibdir}/timereg/help
%{rlibdir}/timereg/data
%{rlibdir}/timereg/R
%{rlibdir}/timereg/Meta
%{rlibdir}/timereg/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.6-1
- initial package for Fedora