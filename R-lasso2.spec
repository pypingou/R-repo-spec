%global packname  lasso2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.12
Release:          1%{?dist}
Summary:          L1 constrained estimation aka `lasso'

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines and documentation for solving regression problems while imposing
an L1 constraint on the estimates, based on the algorithm of Osborne et
al. (1998)

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
%doc %{rlibdir}/lasso2/html
%doc %{rlibdir}/lasso2/DESCRIPTION
%doc %{rlibdir}/lasso2/doc
%{rlibdir}/lasso2/Meta
%{rlibdir}/lasso2/NAMESPACE
%{rlibdir}/lasso2/libs
%{rlibdir}/lasso2/R
%{rlibdir}/lasso2/help
%{rlibdir}/lasso2/INDEX
%{rlibdir}/lasso2/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.12-1
- initial package for Fedora