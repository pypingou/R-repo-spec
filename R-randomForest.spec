%global packname  randomForest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.6.2
Release:          1%{?dist}
Summary:          Breiman and Cutler's random forests for classification and regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Classification and regression based on a forest of trees using random

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
%doc %{rlibdir}/randomForest/CITATION
%doc %{rlibdir}/randomForest/DESCRIPTION
%doc %{rlibdir}/randomForest/html
%doc %{rlibdir}/randomForest/NEWS
%{rlibdir}/randomForest/help
%{rlibdir}/randomForest/Meta
%{rlibdir}/randomForest/data
%{rlibdir}/randomForest/INDEX
%{rlibdir}/randomForest/libs
%{rlibdir}/randomForest/R
%{rlibdir}/randomForest/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.6.2-1
- initial package for Fedora