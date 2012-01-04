%global packname  subselect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11.2
Release:          1%{?dist}
Summary:          Selecting variable subsets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions which (i) assess the quality of variable subsets
as surrogates for a full data set, in either an exploratory data analysis
or in the context of a multivariate linear model, and (ii) search for
subsets which are optimal under various criteria.

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
%doc %{rlibdir}/subselect/doc
%doc %{rlibdir}/subselect/html
%doc %{rlibdir}/subselect/DESCRIPTION
%{rlibdir}/subselect/data
%{rlibdir}/subselect/CHANGELOG
%{rlibdir}/subselect/NAMESPACE
%{rlibdir}/subselect/R
%{rlibdir}/subselect/libs
%{rlibdir}/subselect/Meta
%{rlibdir}/subselect/readme
%{rlibdir}/subselect/INDEX
%{rlibdir}/subselect/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11.2-1
- initial package for Fedora