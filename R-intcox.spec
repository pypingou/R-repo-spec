%global packname  intcox
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Iterated Convex Minorant Algorithm for interval censored event data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Implementation of ICM-Algorithm by Wei Pan, J. Comp. & Gr. Stat. 78:
109-120, 1999 Algorithm for the Cox proportional hazard model for interval
censored data

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
%doc %{rlibdir}/intcox/html
%doc %{rlibdir}/intcox/DESCRIPTION
%doc %{rlibdir}/intcox/doc
%{rlibdir}/intcox/data
%{rlibdir}/intcox/help
%{rlibdir}/intcox/Meta
%{rlibdir}/intcox/INDEX
%{rlibdir}/intcox/R
%{rlibdir}/intcox/libs
%{rlibdir}/intcox/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora