%global packname  pps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.94
Release:          1%{?dist}
Summary:          Functions for PPS sampling

Group:            Applications/Engineering 
License:          GPL version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The pps package contains functions to select samples using PPS
(probability proportional to size) sampling. It also includes a function
for stratified simple random sampling, a function to compute joint
inclusion probabilities for Sampford's method of PPS sampling, and a few
utility functions. The user's guide pps-ug.pdf is included.

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
%doc %{rlibdir}/pps/DESCRIPTION
%doc %{rlibdir}/pps/doc
%doc %{rlibdir}/pps/html
%{rlibdir}/pps/R
%{rlibdir}/pps/INDEX
%{rlibdir}/pps/NAMESPACE
%{rlibdir}/pps/help
%{rlibdir}/pps/data
%{rlibdir}/pps/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.94-1
- initial package for Fedora