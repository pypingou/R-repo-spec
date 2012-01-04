%global packname  dr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.0.7
Release:          1%{?dist}
Summary:          Methods for dimension reduction for regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Functions, methods, and datasets for fitting dimension reduction
regression, using slicing (methods SAVE and SIR), Principal Hessian
Directions (phd, using residuals and the response), and an iterative IRE. 
Partial methods, that condition on categorical predictors are also
available.  A variety of tests, and stepwise deletion of predictors, is
also included.  Also included is code for computing permutation tests of
dimension.  Adding additional methods of estimating dimension is
straightforward.  For documentation, see the vignette in the package. 
With version 3.0.4, the arguments for dr.step have been modified.

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
%doc %{rlibdir}/dr/html
%doc %{rlibdir}/dr/DESCRIPTION
%doc %{rlibdir}/dr/doc
%doc %{rlibdir}/dr/CITATION
%{rlibdir}/dr/R
%{rlibdir}/dr/INDEX
%{rlibdir}/dr/help
%{rlibdir}/dr/NAMESPACE
%{rlibdir}/dr/extdata
%{rlibdir}/dr/Meta
%{rlibdir}/dr/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.7-1
- initial package for Fedora