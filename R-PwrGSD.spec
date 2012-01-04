%global packname  PwrGSD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16
Release:          1%{?dist}
Summary:          Power in a Group Sequential Design

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Tools the evaluation of interim analysis plans for sequentially monitored
trials on a survival endpoint; tools to construct efficacy and futility
boundaries, for deriving power of a sequential design at a specified
alternative, template for evaluating the performance of candidate plans at
a set of time varying alternatives.

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
%doc %{rlibdir}/PwrGSD/html
%doc %{rlibdir}/PwrGSD/DESCRIPTION
%doc %{rlibdir}/PwrGSD/doc
%{rlibdir}/PwrGSD/NAMESPACE
%{rlibdir}/PwrGSD/data
%{rlibdir}/PwrGSD/help
%{rlibdir}/PwrGSD/R
%{rlibdir}/PwrGSD/INDEX
%{rlibdir}/PwrGSD/Meta
%{rlibdir}/PwrGSD/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16-1
- initial package for Fedora