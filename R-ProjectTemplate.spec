%global packname  ProjectTemplate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Automates the creation of new statistical analysis projects.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-testthat 

BuildRequires:    R-devel tex(latex) R-testthat 

%description
ProjectTemplate provides functions to automatically build a directory
structure for a new R project. Using this structure, ProjectTemplate
automates data loading, preprocessing, library importing and unit testing.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora