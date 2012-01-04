%global packname  mosaic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.51
Release:          1%{?dist}
Summary:          Project MOSAIC (mosaic-web.org) math and stats teaching utilities

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-51.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-grid R-methods R-Hmisc 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-methods R-Hmisc 

%description
Data sets and utilities from Project MOSAIC (mosaic-web.org) used to teach
mathematics, statistics, computation and modeling.  Funded by the NSF,
Project MOSAIC is creating a community of educators working to tie
together aspects of quantitative work that students in science,
technology, engineering and mathematics will need in their professional
lives, but which are usually taught in isolation, if at all.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.51-1
- initial package for Fedora