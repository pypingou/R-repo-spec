%global packname  random
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          True random numbers using random.org

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides an interface to the true random number service
provided by the random.org website created by Mads Haahr. The random.org
web service samples atmospheric noise via radio tuned to an unused
broadcasting frequency together with a skew correction algorithm due to
John von Neumann.  More background is available in the included vignette
based on an essay by Mads Haahr. In its current form, the package offers
functions to retrieve random integers, randomized sequences and random

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
%doc %{rlibdir}/random/DESCRIPTION
%doc %{rlibdir}/random/html
%doc %{rlibdir}/random/doc
%{rlibdir}/random/NAMESPACE
%{rlibdir}/random/R
%{rlibdir}/random/Meta
%{rlibdir}/random/INDEX
%{rlibdir}/random/ChangeLog
%{rlibdir}/random/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora