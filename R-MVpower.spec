%global packname  MVpower
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Give power for a given effect size using multivariate classification methods

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest R-pamr R-kernlab R-class 

BuildRequires:    R-devel tex(latex) R-randomForest R-pamr R-kernlab R-class 

%description
Calculate power for a given effect size and sample size using multivariate
classification methods: Random forest (RF), Prediction analysis of
microarrays (PAM), K-nearest neighbor (KNN), or Support vector machine

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
%doc %{rlibdir}/MVpower/html
%doc %{rlibdir}/MVpower/DESCRIPTION
%{rlibdir}/MVpower/NAMESPACE
%{rlibdir}/MVpower/Meta
%{rlibdir}/MVpower/help
%{rlibdir}/MVpower/INDEX
%{rlibdir}/MVpower/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora