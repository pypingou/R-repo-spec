%global packname  Devore7
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.4
Release:          1%{?dist}
Summary:          Data sets from Devore's "Prob and Stat for Eng (7th ed)"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-lattice 

%description
Data sets and sample analyses from Jay L. Devore (2008), "Probability and
Statistics for Engineering and the Sciences (7th ed)", Thomson.

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
%doc %{rlibdir}/Devore7/doc
%doc %{rlibdir}/Devore7/html
%doc %{rlibdir}/Devore7/DESCRIPTION
%doc %{rlibdir}/Devore7/NEWS
%{rlibdir}/Devore7/data
%{rlibdir}/Devore7/INDEX
%{rlibdir}/Devore7/Meta
%{rlibdir}/Devore7/help
%{rlibdir}/Devore7/NAMESPACE
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.4-1
- initial package for Fedora