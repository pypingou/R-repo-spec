%global packname  AUCRF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Variable Selection with Random Forest and the Area Under the Curve

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest 


BuildRequires:    R-devel tex(latex) R-randomForest



%description
Variable selection using Random Forest based on optimizing the
area-under-the ROC curve (AUC) of the Random Forest.

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
%doc %{rlibdir}/AUCRF/DESCRIPTION
%doc %{rlibdir}/AUCRF/html
%{rlibdir}/AUCRF/INDEX
%{rlibdir}/AUCRF/help
%{rlibdir}/AUCRF/NAMESPACE
%{rlibdir}/AUCRF/R
%{rlibdir}/AUCRF/Meta
%{rlibdir}/AUCRF/data

%changelog
* Wed Dec 07 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora