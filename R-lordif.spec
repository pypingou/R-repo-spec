%global packname  lordif
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Logistic Regression Differential Item Functioning using IRT

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-msm R-mvtnorm R-polycor R-sfsmisc R-ltm R-Hmisc R-rms 


BuildRequires:    R-devel tex(latex) R-MASS R-msm R-mvtnorm R-polycor R-sfsmisc R-ltm R-Hmisc R-rms



%description
Analysis of Differential Item Functioning (DIF) for dichotomous and
polytomous items using an iterative hybrid of (ordinal) logistic
regression and item response theory (IRT)

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
%doc %{rlibdir}/lordif/html
%doc %{rlibdir}/lordif/DESCRIPTION
%doc %{rlibdir}/lordif/CITATION
%{rlibdir}/lordif/Meta
%{rlibdir}/lordif/NAMESPACE
%{rlibdir}/lordif/R
%{rlibdir}/lordif/help
%{rlibdir}/lordif/INDEX
%{rlibdir}/lordif/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora