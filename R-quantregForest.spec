%global packname  quantregForest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Quantile Regression Forests

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-randomForest 

BuildRequires:    R-devel tex(latex) R-randomForest 

%description
Quantile Regression Forests is a tree-based ensemble method for estimation
of conditional quantiles. It is particularly well suited for
high-dimensional data. Predictor variables of mixed classes can be
handled. The package is dependent on the package randomForests, written by
Andy Liaw.

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
%doc %{rlibdir}/quantregForest/html
%doc %{rlibdir}/quantregForest/DESCRIPTION
%{rlibdir}/quantregForest/NAMESPACE
%{rlibdir}/quantregForest/INDEX
%{rlibdir}/quantregForest/help
%{rlibdir}/quantregForest/R
%{rlibdir}/quantregForest/Meta
%{rlibdir}/quantregForest/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora