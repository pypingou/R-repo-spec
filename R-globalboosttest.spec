%global packname  globalboosttest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Testing the additional predictive value of high-dimensional data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mboost R-survival 

BuildRequires:    R-devel tex(latex) R-mboost R-survival 

%description
'globalboosttest' implements a permutation-based testing procedure to
globally test the (additional) predictive value of a large set of
predictors given that a small set of predictors is already available.
Currently, 'globalboosttest' supports binary outcomes (via logistic
regression) and survival outcomes (via Cox regression). It is based on
boosting regression as implemented in the package 'mboost'.

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
%doc %{rlibdir}/globalboosttest/DESCRIPTION
%doc %{rlibdir}/globalboosttest/html
%{rlibdir}/globalboosttest/R
%{rlibdir}/globalboosttest/data
%{rlibdir}/globalboosttest/help
%{rlibdir}/globalboosttest/INDEX
%{rlibdir}/globalboosttest/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora