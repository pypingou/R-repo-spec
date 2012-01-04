%global packname  ncomplete
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          ncomplete

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The library contains R-functions to perform the regression depth method
(RDM) to binary regression to approximate the minimum number of
observations that can be removed such that the reduced data set has
complete separation.

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
%doc %{rlibdir}/ncomplete/DESCRIPTION
%doc %{rlibdir}/ncomplete/html
%{rlibdir}/ncomplete/libs
%{rlibdir}/ncomplete/Meta
%{rlibdir}/ncomplete/INDEX
%{rlibdir}/ncomplete/NAMESPACE
%{rlibdir}/ncomplete/help
%{rlibdir}/ncomplete/data
%{rlibdir}/ncomplete/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora