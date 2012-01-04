%global packname  endogMNP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          R Package for Fitting Multinomial Probit Models with Endogenous Selection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
endogMNP is an R package that fits a Bayesian multinomial probit model
with endogenous selection, which is sometimes called an endogenous
switching model.  This can be used to model discrete choice data when
respondents select themselves into one of several groups.  This package is
based on the MNP package by Kosuke Imai and David A. van Dyk.  This
package modifies their code.

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
%doc %{rlibdir}/endogMNP/DESCRIPTION
%doc %{rlibdir}/endogMNP/html
%{rlibdir}/endogMNP/help
%{rlibdir}/endogMNP/Meta
%{rlibdir}/endogMNP/libs
%{rlibdir}/endogMNP/NAMESPACE
%{rlibdir}/endogMNP/INDEX
%{rlibdir}/endogMNP/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora