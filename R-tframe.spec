%global packname  tframe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.1
Release:          1%{?dist}
Summary:          Time Frame coding kernel

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The tframe package provides a kernel of functions for programming time
series methods in a way that is relatively independently of the
representation of time. It also provides plotting, time windowing, and
some other utility functions which are specifically intended for time
series. See the Guide distributed as a vignette, or ?tframe.Intro for more

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
%doc %{rlibdir}/tframe/doc
%doc %{rlibdir}/tframe/DESCRIPTION
%doc %{rlibdir}/tframe/html
%doc %{rlibdir}/tframe/NEWS
%{rlibdir}/tframe/R
%{rlibdir}/tframe/NAMESPACE
%{rlibdir}/tframe/help
%{rlibdir}/tframe/Meta
%{rlibdir}/tframe/INDEX
%{rlibdir}/tframe/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.1-1
- initial package for Fedora