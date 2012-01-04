%global packname  LGS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.91
Release:          1%{?dist}
Summary:          simulating Linkage Group Selection (LGS)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The LGS package simulates the biological steps of a linkage group
selection experiment in order to gain insights into the underlying
biology. See Martinelli et al. (Proc Natl Acad Sci U S A, 2005) for the
LGS experimental procedure and Hunt et al. (BMC Genomics, 2010) for an
application of the simulations implemented in this package.

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
%doc %{rlibdir}/LGS/html
%doc %{rlibdir}/LGS/DESCRIPTION
%{rlibdir}/LGS/R
%{rlibdir}/LGS/help
%{rlibdir}/LGS/INDEX
%{rlibdir}/LGS/data
%{rlibdir}/LGS/NAMESPACE
%{rlibdir}/LGS/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.91-1
- initial package for Fedora