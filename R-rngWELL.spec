%global packname  rngWELL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          toolbox for WELL random number generators.

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
It is a dedicated package to WELL pseudo random generators. But it is not
intended to use it directly, you are strongly __encouraged__ to directly
use the 'randtoolbox' package, which depends on this package.

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
%doc %{rlibdir}/rngWELL/html
%doc %{rlibdir}/rngWELL/CITATION
%doc %{rlibdir}/rngWELL/NEWS
%doc %{rlibdir}/rngWELL/DESCRIPTION
%{rlibdir}/rngWELL/INDEX
%{rlibdir}/rngWELL/NAMESPACE
%{rlibdir}/rngWELL/help
%{rlibdir}/rngWELL/R
%{rlibdir}/rngWELL/LICENSE
%{rlibdir}/rngWELL/Meta
%{rlibdir}/rngWELL/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora