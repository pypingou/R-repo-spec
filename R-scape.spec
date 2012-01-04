%global packname  scape
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Statistical Catch-at-Age Plotting Environment

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Hmisc R-lattice 

BuildRequires:    R-devel tex(latex) R-Hmisc R-lattice 

%description
Import, plot, and diagnose results from statistical catch-at-age models,
used in fisheries stock assessment.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora