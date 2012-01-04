%global packname  reldist
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Relative Distribution Methods

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R functions for the comparison of distributions. This includes
nonparametric estimation of the relative distribution PDF and CDF and
numerical summaries as described in "Relative Distribution Methods in the
Social Sciences" by Mark S. Handcock and Martina Morris, Springer-Verlag,
1999, Springer-Verlag, ISBN 0387987789

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
%doc %{rlibdir}/reldist/html
%doc %{rlibdir}/reldist/DESCRIPTION
%doc %{rlibdir}/reldist/CITATION
%{rlibdir}/reldist/Meta
%{rlibdir}/reldist/R
%{rlibdir}/reldist/data
%{rlibdir}/reldist/help
%{rlibdir}/reldist/NAMESPACE
%{rlibdir}/reldist/LICENSE
%{rlibdir}/reldist/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora