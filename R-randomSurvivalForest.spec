%global packname  randomSurvivalForest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.6.3
Release:          1%{?dist}
Summary:          Random Survival Forests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Random survival forests for right-censored and competing risks survival

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
%doc %{rlibdir}/randomSurvivalForest/doc
%doc %{rlibdir}/randomSurvivalForest/NEWS
%doc %{rlibdir}/randomSurvivalForest/DESCRIPTION
%doc %{rlibdir}/randomSurvivalForest/html
%doc %{rlibdir}/randomSurvivalForest/CITATION
%{rlibdir}/randomSurvivalForest/Meta
%{rlibdir}/randomSurvivalForest/NAMESPACE
%{rlibdir}/randomSurvivalForest/libs
%{rlibdir}/randomSurvivalForest/R
%{rlibdir}/randomSurvivalForest/help
%{rlibdir}/randomSurvivalForest/INDEX
%{rlibdir}/randomSurvivalForest/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.6.3-1
- initial package for Fedora