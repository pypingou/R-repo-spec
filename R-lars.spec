%global packname  lars
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.8
Release:          1%{?dist}
Summary:          Least Angle Regression, Lasso and Forward Stagewise

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Efficient procedures for fitting an entire lasso sequence with the cost of
a single least squares fit. Least angle regression and infinitessimal
forward stagewise regression are related to the lasso, as described in the
paper below.

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
%doc %{rlibdir}/lars/DESCRIPTION
%doc %{rlibdir}/lars/html
%{rlibdir}/lars/INDEX
%{rlibdir}/lars/data
%{rlibdir}/lars/R
%{rlibdir}/lars/NAMESPACE
%{rlibdir}/lars/libs
%{rlibdir}/lars/Meta
%{rlibdir}/lars/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.8-1
- initial package for Fedora