%global packname  fastmatch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Fast match() function

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package providing a fast match() replacement for cases that require
repeated look-ups. It is slightly faster that R's built-in match()
function on first match against a table, but extremely fast on any
subsequent lookup as it keeps the hash table in memory.

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
%doc %{rlibdir}/fastmatch/html
%doc %{rlibdir}/fastmatch/NEWS
%doc %{rlibdir}/fastmatch/DESCRIPTION
%{rlibdir}/fastmatch/NAMESPACE
%{rlibdir}/fastmatch/INDEX
%{rlibdir}/fastmatch/help
%{rlibdir}/fastmatch/Meta
%{rlibdir}/fastmatch/R
%{rlibdir}/fastmatch/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora