%global packname  cvplogistic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Majorization Minimization by Coordinate Descent Algorithm for Concave Penalized Logistic Regression for High Dimensional Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package uses majorization minimization by coordinate descent (MMCD)
algorithm to compute the solution surface for concave penalized logistic
regression models. The SCAD and MCP (default) are two concave penalties
considered in this implementation. The package provides three types of
solutions surfaces, one computed along the regulation parameter kappa
(default), the one along the penalty parameter lambda, and the one
computed using a hybrid algorithm. The package also provides three tuning
parameter selection methods, one based on AIC, one based on BIC and one
based on k-fold Cross-validated AUC.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora