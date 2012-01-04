%global packname  ltm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Latent Trait Models under IRT

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-msm R-mvtnorm R-polycor 

BuildRequires:    R-devel tex(latex) R-MASS R-msm R-mvtnorm R-polycor 

%description
Analysis of multivariate dichotomous and polytomous data using latent
trait models under the Item Response Theory approach. It includes the
Rasch, the Two-Parameter Logistic, the Birnbaum's Three-Parameter, the
Graded Response, and the Generalized Partial Credit Models.

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
%doc %{rlibdir}/ltm/NEWS
%doc %{rlibdir}/ltm/html
%doc %{rlibdir}/ltm/DESCRIPTION
%doc %{rlibdir}/ltm/CITATION
%{rlibdir}/ltm/data
%{rlibdir}/ltm/INDEX
%{rlibdir}/ltm/help
%{rlibdir}/ltm/Meta
%{rlibdir}/ltm/NAMESPACE
%{rlibdir}/ltm/demo
%{rlibdir}/ltm/R

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.7-1
- initial package for Fedora