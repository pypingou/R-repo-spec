%global packname  lme4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.999375.42
Release:          1%{?dist}
Summary:          Linear mixed-effects models using S4 classes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.999375-42.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Matrix R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-Matrix R-lattice 

%description
Fit linear and generalized linear mixed-effects models.

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
%doc %{rlibdir}/lme4/html
%doc %{rlibdir}/lme4/doc
%doc %{rlibdir}/lme4/NEWS
%doc %{rlibdir}/lme4/DESCRIPTION
%{rlibdir}/lme4/libs
%{rlibdir}/lme4/Meta
%{rlibdir}/lme4/data
%{rlibdir}/lme4/R
%{rlibdir}/lme4/NAMESPACE
%{rlibdir}/lme4/help
%{rlibdir}/lme4/INDEX
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.999375.42-1
- initial package for Fedora