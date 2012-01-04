%global packname  TeachingDemos
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.7
Release:          1%{?dist}
Summary:          Demonstrations for teaching and learning

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is a set of demonstration functions that can be used in a
classroom to demonstrate statistical concepts, or on your own to better
understand the concepts or the programming.

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
%doc %{rlibdir}/TeachingDemos/NEWS
%doc %{rlibdir}/TeachingDemos/html
%doc %{rlibdir}/TeachingDemos/DESCRIPTION
%{rlibdir}/TeachingDemos/help
%{rlibdir}/TeachingDemos/data
%{rlibdir}/TeachingDemos/INDEX
%{rlibdir}/TeachingDemos/R
%{rlibdir}/TeachingDemos/Meta
%{rlibdir}/TeachingDemos/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.7-1
- initial package for Fedora