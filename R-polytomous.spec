%global packname  polytomous
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Polytomous logistic regression for fixed and mixed effects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-MASS R-Hmisc R-lme4 


BuildRequires:    R-devel tex(latex) R-stats R-MASS R-Hmisc R-lme4



%description
Logistic regression modeling for polytomous settings (more than two
categorical outcomes) with both fixed and mixed effect predictors, and
univariate analysis of categorical, unordered data.

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
%doc %{rlibdir}/polytomous/DESCRIPTION
%doc %{rlibdir}/polytomous/html
%{rlibdir}/polytomous/NAMESPACE
%{rlibdir}/polytomous/help
%{rlibdir}/polytomous/Meta
%{rlibdir}/polytomous/INDEX
%{rlibdir}/polytomous/data
%{rlibdir}/polytomous/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora