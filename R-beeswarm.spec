%global packname  beeswarm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          The bee swarm plot, an alternative to stripchart

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The bee swarm plot is a one-dimensional scatter plot like "stripchart",
but with closely-packed, non-overlapping points.

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
%doc %{rlibdir}/beeswarm/NEWS
%doc %{rlibdir}/beeswarm/DESCRIPTION
%doc %{rlibdir}/beeswarm/html
%{rlibdir}/beeswarm/INDEX
%{rlibdir}/beeswarm/R
%{rlibdir}/beeswarm/NAMESPACE
%{rlibdir}/beeswarm/data
%{rlibdir}/beeswarm/Meta
%{rlibdir}/beeswarm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora