%global packname  ucminf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          General-purpose unconstrained non-linear optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An algorithm for general-purpose unconstrained non-linear optimization.
The algorithm is of quasi-Newton type with BFGS updating of the inverse
Hessian and soft line search with a trust region type monitoring of the
input to the line search algorithm. The interface of 'ucminf' is designed
for easy interchange with 'optim'.

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
%doc %{rlibdir}/ucminf/html
%doc %{rlibdir}/ucminf/DESCRIPTION
%doc %{rlibdir}/ucminf/doc
%{rlibdir}/ucminf/INDEX
%{rlibdir}/ucminf/help
%{rlibdir}/ucminf/Meta
%{rlibdir}/ucminf/libs
%{rlibdir}/ucminf/NAMESPACE
%{rlibdir}/ucminf/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora