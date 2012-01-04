%global packname  grpreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Regularization paths for regression models with grouped covariates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Efficient algorithms for fitting the regularization path for linear or
logistic regression models penalized by the group lasso, group bridge, or
group MCP methods.  The algorithm is based on the idea of a locally
approximated coordinate descent.

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
%doc %{rlibdir}/grpreg/NEWS
%doc %{rlibdir}/grpreg/html
%doc %{rlibdir}/grpreg/CITATION
%doc %{rlibdir}/grpreg/DESCRIPTION
%{rlibdir}/grpreg/data
%{rlibdir}/grpreg/libs
%{rlibdir}/grpreg/Meta
%{rlibdir}/grpreg/NAMESPACE
%{rlibdir}/grpreg/R
%{rlibdir}/grpreg/INDEX
%{rlibdir}/grpreg/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora