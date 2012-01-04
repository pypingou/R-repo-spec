%global packname  adabag
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Applies Adaboost.M1 and Bagging

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rpart R-mlbench 

BuildRequires:    R-devel tex(latex) R-rpart R-mlbench 

%description
This package implements Freund and Schapire's Adaboost.M1 algorithm and
Breiman's Bagging algorithm using classification trees as individual
classifiers. Once these classifiers have been trained, they can be used to
predict on new data. Also, cross validation predictions can be done.  This
version 2.0 adds a new function "margins" to calculate the margins for
these classifiers.  Also a higher flexibility is achieved giving access to
the "rpart.control" argument of "rpart".

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
%doc %{rlibdir}/adabag/html
%doc %{rlibdir}/adabag/DESCRIPTION
%{rlibdir}/adabag/Meta
%{rlibdir}/adabag/INDEX
%{rlibdir}/adabag/help
%{rlibdir}/adabag/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora