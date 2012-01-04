%global packname  bst
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Gradient Boosting

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rpart 

BuildRequires:    R-devel tex(latex) R-rpart 

%description
The package contains HingeBoost for binary and multi-class classification
with unequal misclassification costs. Functional gradient descent
algorithm to optimize the cost-sensitive hinge loss. The algorithm can fit
linear classifier with linear least squares, nonlinear classifer with
smoothing spline (or trees) as base learner.

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
%doc %{rlibdir}/bst/html
%doc %{rlibdir}/bst/NEWS
%doc %{rlibdir}/bst/DESCRIPTION
%{rlibdir}/bst/R
%{rlibdir}/bst/NAMESPACE
%{rlibdir}/bst/help
%{rlibdir}/bst/INDEX
%{rlibdir}/bst/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora