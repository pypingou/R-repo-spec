%global packname  CORElearn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.35
Release:          1%{?dist}
Summary:          CORElearn - classification, regression, feature evaluation and ordinal evaluation

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-rpart R-stats 

BuildRequires:    R-devel tex(latex) R-cluster R-rpart R-stats 

%description
CORElearn is machine learning suite ported to R from standalone C++
package. It contains several model learning techniques in classification
and regression, for example classification and regression trees with
optional constructive induction and models in the leafs, random forests,
kNN, naive Bayes, and locally weighted regression. It is especially strong
in feature evaluation algorithms where it contains several variants of
Relief algorithm and many impurity based attribute evaluation functions,
e.g., Gini, information gain, MDL, DKM, ... Its additional strength is
ordEval algorithm and its visualization used for ordinal features and
class. Several algorithms support parallel multithreaded execution via
OpenMP. Windows binary versions supporting multithreading are available on
package website, as CRAN uses different toolchain. The top level
documentation is reachable through ?CORElearn.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.35-1
- initial package for Fedora