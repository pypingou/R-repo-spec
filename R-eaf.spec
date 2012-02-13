%global packname  eaf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04
Release:          1%{dist}
Summary:          Plots of the Empirical Attainment Function

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-modeltools 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-modeltools 


%description
Plots of the empirical attainment function for two objectives.

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
%doc %{rlibdir}/eaf/CITATION
%doc %{rlibdir}/eaf/DESCRIPTION
%doc %{rlibdir}/eaf/html
%doc %{rlibdir}/eaf/NEWS
%{rlibdir}/eaf/help
%{rlibdir}/eaf/R
%{rlibdir}/eaf/data
%{rlibdir}/eaf/INDEX
%{rlibdir}/eaf/scripts
%{rlibdir}/eaf/NAMESPACE
%{rlibdir}/eaf/extdata
%{rlibdir}/eaf/Meta
%{rlibdir}/eaf/libs

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04-1
- Update to version 1.04

* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora