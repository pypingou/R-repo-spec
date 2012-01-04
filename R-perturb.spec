%global packname  perturb
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.04
Release:          1%{?dist}
Summary:          Tools for evaluating collinearity

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
"perturb" evaluates collinearity by adding random noise to selected
variables. "colldiag" calculates condition numbers and variance
decomposition proportions to test for collinearity and uncover its

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
%doc %{rlibdir}/perturb/html
%doc %{rlibdir}/perturb/DESCRIPTION
%{rlibdir}/perturb/NAMESPACE
%{rlibdir}/perturb/Meta
%{rlibdir}/perturb/INDEX
%{rlibdir}/perturb/R
%{rlibdir}/perturb/help
%{rlibdir}/perturb/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.04-1
- initial package for Fedora