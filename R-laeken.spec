%global packname  laeken
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Estimation of indicators on social exclusion and poverty

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-MASS 

BuildRequires:    R-devel tex(latex) R-boot R-MASS 

%description
Estimation of indicators on social exclusion and poverty, as well as
Pareto tail modeling for empirical income distributions (including
graphical tools).

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
%doc %{rlibdir}/laeken/doc
%doc %{rlibdir}/laeken/DESCRIPTION
%doc %{rlibdir}/laeken/CITATION
%doc %{rlibdir}/laeken/html
%doc %{rlibdir}/laeken/NEWS
%{rlibdir}/laeken/NAMESPACE
%{rlibdir}/laeken/Meta
%{rlibdir}/laeken/INDEX
%{rlibdir}/laeken/R
%{rlibdir}/laeken/help
%{rlibdir}/laeken/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora