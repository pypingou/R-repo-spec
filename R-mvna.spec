%global packname  mvna
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Nelson-Aalen estimator of the cumulative hazard in multistate models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
This package computes the Nelson-Aalen estimator of the cumulative
transition hazard for multistate models.

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
%doc %{rlibdir}/mvna/CITATION
%doc %{rlibdir}/mvna/DESCRIPTION
%doc %{rlibdir}/mvna/html
%{rlibdir}/mvna/R
%{rlibdir}/mvna/libs
%{rlibdir}/mvna/data
%{rlibdir}/mvna/NAMESPACE
%{rlibdir}/mvna/help
%{rlibdir}/mvna/Meta
%{rlibdir}/mvna/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora