%global packname  sm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.4.1
Release:          1%{?dist}
Summary:          Smoothing methods for nonparametric regression and density estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-4.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is software linked to the book `Applied Smoothing Techniques for Data
Analysis: The Kernel Approach with S-Plus Illustrations' Oxford University

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
%doc %{rlibdir}/sm/CITATION
%doc %{rlibdir}/sm/DESCRIPTION
%doc %{rlibdir}/sm/html
%doc %{rlibdir}/sm/COPYING
%{rlibdir}/sm/R
%{rlibdir}/sm/INDEX
%{rlibdir}/sm/help
%{rlibdir}/sm/Meta
%{rlibdir}/sm/scripts
%{rlibdir}/sm/data
%{rlibdir}/sm/NAMESPACE
%{rlibdir}/sm/history.txt
%{rlibdir}/sm/smdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.4.1-1
- initial package for Fedora