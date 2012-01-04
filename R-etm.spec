%global packname  etm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Empirical Transition Matrix

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-survival 

BuildRequires:    R-devel tex(latex) R-lattice R-survival 

%description
Matrix of transition probabilities for any time-inhomogeneous multistate
model with finite state space

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
%doc %{rlibdir}/etm/CITATION
%doc %{rlibdir}/etm/DESCRIPTION
%doc %{rlibdir}/etm/doc
%doc %{rlibdir}/etm/html
%{rlibdir}/etm/NAMESPACE
%{rlibdir}/etm/Meta
%{rlibdir}/etm/libs
%{rlibdir}/etm/help
%{rlibdir}/etm/R
%{rlibdir}/etm/data
%{rlibdir}/etm/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora