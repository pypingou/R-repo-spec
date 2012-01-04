%global packname  optmatch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Functions for optimal matching

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions for optimal matching, including full matching

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
%doc %{rlibdir}/optmatch/CITATION
%doc %{rlibdir}/optmatch/DESCRIPTION
%doc %{rlibdir}/optmatch/html
%doc %{rlibdir}/optmatch/NEWS
%{rlibdir}/optmatch/LICENSE
%{rlibdir}/optmatch/NAMESPACE
%{rlibdir}/optmatch/help
%{rlibdir}/optmatch/INDEX
%{rlibdir}/optmatch/Meta
%{rlibdir}/optmatch/data
%{rlibdir}/optmatch/R
%{rlibdir}/optmatch/libs
%{rlibdir}/optmatch/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora